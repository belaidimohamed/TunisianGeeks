import { AlertifyService } from './../_services/alertify.service';
import { ProjectFormComponent } from './../_forms/projectForm/projectForm.component';
import { ApiPostService } from './../_services/apiPost.service';
import { ApiGetService } from './../_services/apiGet.service';
import { Component, OnInit } from '@angular/core';
import { MatDialogConfig, MatDialog } from '@angular/material';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-side-nav',
  templateUrl: './side-nav.component.html',
  styleUrls: ['./side-nav.component.css']
})
export class SideNavComponent implements OnInit {
  fieldId: number ;
  projects: any = {} ;
  currentProject: any = {} ;
  constructor(private route: ActivatedRoute, private apiGetService: ApiGetService  ,
                private dialog: MatDialog , private alertify: AlertifyService) {}

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.fieldId = params.id;
      this.getProjects(this.fieldId); });
  }
  getProjects(id: number) {
    this.apiGetService.getProjects(id).subscribe( data => {this.projects = data ;
                                                           this.projects = Array.of(JSON.parse(this.projects));
                                                          },
                                                  error => {this.alertify.error(error); });
  }
  openProjectForm() {
    const dialogconfig = new MatDialogConfig() ;
    dialogconfig.disableClose = true ;
    dialogconfig.autoFocus = true ;
    dialogconfig.width = '60%';
    dialogconfig.data = {id: this.fieldId };
    this.dialog.open(ProjectFormComponent, dialogconfig).afterClosed().subscribe(next => {
      this.apiGetService.getProjects(this.fieldId).subscribe( data => {this.projects = data ;
                                                                       this.projects = Array.of(JSON.parse(this.projects)); },
                                                              error => {this.alertify.error(error); });
    });
  }
 

}
