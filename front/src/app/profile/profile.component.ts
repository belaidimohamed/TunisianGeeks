import { AlertifyService } from './../_services/alertify.service';
import { AuthService } from './../_services/auth.service';
import { SkillFormComponent } from './../_forms/skillForm/skillForm.component';
import { ApiPostService } from 'src/app/_services/apiPost.service';
import { ApiGetService } from './../_services/apiGet.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MatDialogConfig , MatDialog } from '@angular/material';
import { GlobalConstants } from '../global-constants';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  minDate = new Date(2000, 1);
  maxDate = new Date(2029, 1);
  onaddSkill = false ;
  educShow = false ;
  devMode = true ; /* if the user is owner he can choose how to see his profile dev mode or no */
  expShow = false ;
  model: any = {} ;
  infos: any = {};
  id: string ;
  skillJson: any = {};
  skillkeys: any ;
  skill: string ;
  percent: number ;
  educations: any ;
  baseUrl = GlobalConstants.apiURL ;
  constructor( private route: ActivatedRoute, private apiGet: ApiGetService, private alertify: AlertifyService,
               private apiPost: ApiPostService , private dialog: MatDialog ,
               private api: ApiGetService , private authService: AuthService, ) { }

  ngOnInit() {
    this.infos = JSON.parse(this.route.snapshot.data.profile) ;
    this.educations = this.JsonPipe(this.infos.education);
    console.log(this.educations);
  }
  loggedIn() {
    return  this.authService.loggedIn();
  }
  isOwnerIsloggin() {
    this.route.params.subscribe(data => { this.id = data.uid; });
    if ( this.loggedIn() ) {
      if ( this.id == localStorage.getItem('id') ) {
        return true;
      }
    } else {
        return false ;
    }
  }
  developerMode() {
    this.devMode = !this.devMode ;
    return this.devMode ;
  }
  JsonPipe(data: string) {
    // tslint:disable-next-line: triple-equals
    if (data == '{}') {
      return null;
    } else {
      return [JSON.parse(data) , Object.keys(JSON.parse(data))] ;
    }
  }
  addEducation() {
    console.log(this.model.description);
    if (!this.model.title || !this.model.degree || !this.model.startDate || !this.model.endDate) {
      this.alertify.warning('You should fill al the fileds before saving');
      return false;
    }
    const modelJ = new FormData();
    modelJ.append('title', this.model.title);
    modelJ.append('degree', this.model.degree);
    modelJ.append('description', this.model.description);
    modelJ.append('startDate', this.model.startDate);
    modelJ.append('endDate', this.model.endDate);
    // tslint:disable-next-line: radix
    this.apiPost.addEduc(modelJ, parseInt(localStorage.getItem('id'))).subscribe(
      next => { this.educShow = false ;
                this.alertify.success('Education added succefully ');
              },
      error => {
        this.alertify.error(error.detail);
        console.log(error.detail);
      });
  }
  openSkillForm(cle: number) {
    const dialogconfig = new MatDialogConfig() ;
    dialogconfig.disableClose = true ;
    dialogconfig.autoFocus = true ;
    dialogconfig.width = '60%';
    dialogconfig.data = {key: cle};
    this.dialog.open(SkillFormComponent, dialogconfig).afterClosed().subscribe(next => {
      // tslint:disable-next-line: radix
    this.api.getProfile(parseInt(localStorage.getItem('id'))).subscribe((results: string) => {
          this.infos = JSON.parse(results);
        });
    });
  }
}
