import { Router } from '@angular/router';
import { ApiGetService } from './../_services/apiGet.service';
import { FieldFormComponent } from './../_forms/fieldForm/fieldForm.component';
import { AlertifyService } from './../_services/alertify.service';
import { RegisterComponent } from './../_forms/register/register.component';
import { AuthService } from './../_services/auth.service';
import { Component, OnInit } from '@angular/core';
import { MatDialog , MatDialogConfig } from '@angular/material' ;
import { EditProfileComponent } from '../_forms/editProfile/editProfile.component';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {
  uid = localStorage.getItem('id');
  model: any = {} ;
  loginclicked: any = false ;
  decodedToken: any ;
  fields: any = {} ;
  constructor(public authService: AuthService,
              private dialog: MatDialog ,
              private alertify: AlertifyService,
              private apiGetService: ApiGetService ,
              private router: Router
  ) { }


  ngOnInit() { 
    this.GetFields() ;
  }

  GetFields() {
    if (this.loggedIn()) {
      this.apiGetService.getFields().subscribe(data => {
        this.fields = data;
        this.fields = Array.of(JSON.parse(this.fields));
      }
        , error => {console.log(error); this.alertify.error(error); } ) ;
       }
  }

  login() {
    this.authService.login(this.model).subscribe(next => {   this.GetFields();
                                                            ;this.alertify.success('logged in succefully ! '); },
                                                error => {console.log(error.non_field_errors);
                                                          this.alertify.error(error.non_field_errors[0]); }
    );
  }
  loggedIn() {
    return  this.authService.loggedIn();
  }
  loginClicked() {
    this.loginclicked = !this.loginclicked ;
    return this.loginClicked ;
  }
  logout() {
    localStorage.removeItem('name');
    localStorage.removeItem('token');
    localStorage.removeItem('id');
    this.router.navigate(['\home']);
    this.alertify.success('logged out') ;
  }
 

  openRegisterForm() {
    const dialogconfig = new MatDialogConfig() ;
    dialogconfig.disableClose = true ;
    dialogconfig.autoFocus = true ;
    dialogconfig.width = '60%';
    this.dialog.open(RegisterComponent, dialogconfig);
  }
  openFieldForm() {
    const dialogconfig = new MatDialogConfig() ;
    dialogconfig.autoFocus = true ;
    dialogconfig.width = '60%';
    this.dialog.open(FieldFormComponent, dialogconfig).afterClosed().subscribe( next=> {
      this.GetFields();
    });
  }
  openEditProfileForm() {
    console.log('paw');
    const dialogconfig = new MatDialogConfig() ;
    dialogconfig.disableClose = true ;
    dialogconfig.autoFocus = true ;
    dialogconfig.width = '60%';
    // dialogconfig.data = {id: this.fieldId };
    this.dialog.open(EditProfileComponent, dialogconfig);
  }
  

}
