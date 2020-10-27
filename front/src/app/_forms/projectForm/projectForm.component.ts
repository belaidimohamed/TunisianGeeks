import { Component, OnInit, Inject } from '@angular/core';
import { ApiPostService } from 'src/app/_services/apiPost.service';
import { MatDialog } from '@angular/material';
import { AlertifyService } from 'src/app/_services/alertify.service';
import {MAT_DIALOG_DATA} from '@angular/material/dialog';


@Component({
  selector: 'app-projectForm',
  templateUrl: './projectForm.component.html',
  styleUrls: ['./projectForm.component.css']
})
export class ProjectFormComponent implements OnInit {
  file: File;
  title: string ;
  bugs: string ;
  description: string ;
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
  onTitleChange(event: any) {
    this.title = event.target.value;

  }
  onDescriptionChange(event: any) {
    this.description = event.target.value;
  }
  onBugsChange(event: any) {
    this.bugs = event.target.value;
  }
  addProject() {
    const model = new FormData();
    model.append('field', this.data.id)  ;
    model.append('title', this.title)  ;
    model.append('description', this.description)  ;
    model.append('code_file', this.file , this.file.name);

    model.append('bugs', this.bugs)  ;


    this.apiPostService.AddProject(model).subscribe(
      res => {  this.cancelForm();
                this.alertify.success('Project added successfully'); },
      error => {
        console.log(error);
        this.cancelForm();
        this.alertify.error(error); }
    );
}
}
