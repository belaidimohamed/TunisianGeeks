import { AuthService } from './../_services/auth.service';
import { SkillFormComponent } from './../_forms/skillForm/skillForm.component';
import { ApiPostService } from 'src/app/_services/apiPost.service';
import { ApiGetService } from './../_services/apiGet.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MatDialogConfig , MatDialog } from '@angular/material';
import { GlobalConstants } from '../global-constants';
import {FormGroup, FormControl} from '@angular/forms';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  onaddSkill = false ;
  model: any = {} ;
  infos: any = {};
  id: string ;
  skillJson: any = {};
  skillkeys: any ;
  skill: string ;
  percent: number ;
  baseUrl = GlobalConstants.apiURL ;
  range = new FormGroup({
    start: new FormControl(),
    end: new FormControl()
  });
  constructor( private route: ActivatedRoute, private apiGet: ApiGetService,
               private apiPost: ApiPostService , private dialog: MatDialog ,
               private api: ApiGetService , private authService: AuthService, ) { }

  ngOnInit() {
    this.infos = JSON.parse(this.route.snapshot.data.profile) ;
    console.log(this.infos);
    console.log(this.JsonPipe(this.infos.education));
  }
  loggedIn() {
    return  this.authService.loggedIn();
  }
  isOwnerIsloggin() {
    this.route.params.subscribe(data => { this.id = data.uid; });
    if ( this.loggedIn() ) {
      if ( this.id == localStorage.getItem('id') ) {
        return true;
      }}
    return false ;
  }
  JsonPipe(data: string) {
    // tslint:disable-next-line: triple-equals
    if (data == '{}') {
      return null;
    } else {
      // console.log(JSON.parse(data));
      // console.log( Object.keys(JSON.parse(data)));
      return [JSON.parse(data) , Object.keys(JSON.parse(data))] ;
    }
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
