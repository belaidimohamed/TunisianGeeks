import { AlertifyService } from './../_services/alertify.service';
import { AuthService } from './../_services/auth.service';
import { SkillFormComponent } from './../_forms/skillForm/skillForm.component';
import { ApiPostService } from 'src/app/_services/apiPost.service';
import { ApiGetService } from './../_services/apiGet.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MatDialogConfig , MatDialog } from '@angular/material';
import { GlobalConstants } from '../global-constants';
import {COMMA, ENTER} from '@angular/cdk/keycodes';
import {MatChipInputEvent} from '@angular/material/chips';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  visible = true;
  selectable = true;
  removable = true;
  addOnBlur = true;
  readonly separatorKeysCodes: number[] = [ENTER, COMMA];
  descriptions = [];


  minDate = new Date(2000, 1);
  maxDate = new Date(2029, 1);
  onaddSkill = false ;
  educShow = false ;
  devMode = true ; /* if the user is owner he can choose how to see his profile dev mode or no */
  expShow = false ;
  EdModel: any = {} ;
  ExpModel: any = {} ;
  infos: any = {};
  id: string ;
  skillJson: any = {};
  skillkeys: any ;
  skill: string ;
  percent: number ;
  educations: any ;
  experiences: any ;
  baseUrl = GlobalConstants.apiURL ;
  constructor( private route: ActivatedRoute, private alertify: AlertifyService,
               private apiPost: ApiPostService , private dialog: MatDialog ,
               private apiGet: ApiGetService , private authService: AuthService, ) { }

  ngOnInit() {
    this.infos = JSON.parse(this.route.snapshot.data.profile) ;
    this.educations = this.JsonPipe(this.infos.education);
    this.experiences = this.JsonPipe(this.infos.experience);
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
  stringtolist(data: string) {
    return JSON.parse(data);
  }
  addEducation() {
    console.log(this.EdModel.description);
    if (!this.EdModel.title || !this.EdModel.degree || !this.EdModel.startDate || !this.EdModel.endDate) {
      this.alertify.warning('You should fill al the fileds before saving');
      return false;
    }
    const modelJ = new FormData();
    modelJ.append('title', this.EdModel.title);
    modelJ.append('degree', this.EdModel.degree);
    modelJ.append('description', this.EdModel.description);
    modelJ.append('startDate', this.EdModel.startDate);
    modelJ.append('endDate', this.EdModel.endDate);
    // tslint:disable-next-line: radix
    this.apiPost.addEduc(modelJ, parseInt(localStorage.getItem('id'))).subscribe(
      next => { 
                this.apiGet.getProfile(parseInt(localStorage.getItem('id'))).subscribe((results: string) => {
                  this.infos = JSON.parse(results);
                  this.educations = this.JsonPipe(this.infos.education);
                });
                this.educShow = false ;
                this.alertify.success('Education added succefully ');
              },
      error => {
        this.alertify.error(error.detail);
        console.log(error.detail);
      });
  }
  addExperience() {
    // tslint:disable-next-line: max-line-length
    if (!this.ExpModel.jobTitle || !this.ExpModel.employer || !this.ExpModel.location || !this.ExpModel.startDate ) {
      this.alertify.warning('You should fill al the fileds before saving');
      return false;
    }
    if (!this.ExpModel.endDate ) {
      this.ExpModel.endDate = null ;
    }
    const modelJ = new FormData();
    modelJ.append('jobTitle', this.ExpModel.jobTitle);
    modelJ.append('employer', this.ExpModel.employer);
    modelJ.append('location', this.ExpModel.location);
    modelJ.append('startDate', this.ExpModel.startDate);
    modelJ.append('endDate', this.ExpModel.endDate);
    modelJ.append('description', JSON.stringify(this.descriptions));
    // tslint:disable-next-line: radix
    this.apiPost.addExp(modelJ, parseInt(localStorage.getItem('id'))).subscribe(
      next => { 
                this.apiGet.getProfile(parseInt(localStorage.getItem('id'))).subscribe((results: string) => {
                  this.infos = JSON.parse(results);
                  this.experiences = this.JsonPipe(this.infos.experience);
                });
                this.educShow = false ;
                this.alertify.success('Job added succefully ');
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
    this.apiGet.getProfile(parseInt(localStorage.getItem('id'))).subscribe((results: string) => {
          this.infos = JSON.parse(results);
        });
    });
  }
/* -------------------------------------- little chips shit ----------------------------------------------------*/
  add(event: MatChipInputEvent): void {
    const input = event.input;
    const value = event.value;

    // Add our fruit
    if ((value || '').trim()) {
      this.descriptions.push({name: value.trim()});
    }

    // Reset the input value
    if (input) {
      input.value = '';
    }
  }

  remove(decr: any): void {
    const index = this.descriptions.indexOf(decr);

    if (index >= 0) {
      this.descriptions.splice(index, 1);
    }
  }
}
