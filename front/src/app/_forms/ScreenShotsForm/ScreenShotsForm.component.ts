import { Component, OnInit, Inject } from '@angular/core';
import { ApiPostService } from 'src/app/_services/apiPost.service';
import { MatDialog } from '@angular/material';
import { AlertifyService } from 'src/app/_services/alertify.service';
import {MAT_DIALOG_DATA} from '@angular/material/dialog';

@Component({
  // tslint:disable-next-line: component-selector
  selector: 'app-ScreenShotsForm',
  templateUrl: './ScreenShotsForm.component.html',
  styleUrls: ['./ScreenShotsForm.component.scss']
})
export class ScreenShotsFormComponent implements OnInit {
  file: File;
  legend: string ;
  constructor(private apiPostService: ApiPostService , private dialog: MatDialog , private alertify: AlertifyService
    ,         @Inject(MAT_DIALOG_DATA) public data: any) { }

  ngOnInit() {
  }
  cancelForm() {
    this.dialog.closeAll() ;
  }
  onFileChange(event: any) {
    this.file =  event.target.files[0];
  }
  onLegendChange(event: any) {
    this.legend = event.target.value;
  }
  addProject() {
    const model = new FormData();
    model.append('project', this.data.id)  ;
    model.append('legend', this.legend)  ;
    model.append('image', this.file , this.file.name);

    this.apiPostService.AddScreenShot(model).subscribe(
      res => {  this.cancelForm();
                this.alertify.success('Screen shot added successfully'); },
      error => {
        console.log(error);
        this.cancelForm();
        this.alertify.error(error); }
    );
}
}
