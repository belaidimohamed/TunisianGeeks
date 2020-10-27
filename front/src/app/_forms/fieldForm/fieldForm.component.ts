import { AlertifyService } from '../../_services/alertify.service';
import { ApiPostService } from '../../_services/apiPost.service';
import { Component, OnInit} from '@angular/core';
import { MatDialog } from '@angular/material';

@Component({
  selector: 'app-fieldForm',
  templateUrl: './fieldForm.component.html',
  styleUrls: ['./fieldForm.component.css']
})
export class FieldFormComponent implements OnInit {
  model: any = {} ;
  constructor(private apiPostService: ApiPostService , private dialog: MatDialog , private alertify: AlertifyService,
              ) { }

  ngOnInit() {
  }

  cancelField() {
    this.dialog.closeAll() ;
  }
  addField() {
    this.model.user = localStorage.getItem('id')  ;
    this.apiPostService.AddField(this.model).subscribe(
      () => { this.cancelField();
              this.alertify.success('Field added successfully'); },
      error => {
        console.log(error);
        this.cancelField();
        this.alertify.error(error); }
    );
  }

}
