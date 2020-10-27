import { AlertifyService } from './../../_services/alertify.service';
import { Component, OnInit } from '@angular/core';
import { AuthService } from './../../_services/auth.service';
import { MatDialogConfig, MatDialog } from '@angular/material';
import { EditProfileComponent } from '../editProfile/editProfile.component';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  model: any = {} ;
  constructor(private authService: AuthService , private dialog: MatDialog , private alertify: AlertifyService) { }

  ngOnInit() {
  }
  cancelRegister() {
    this.dialog.closeAll() ;
  }
  openEditProfileForm() {
    const dialogconfig = new MatDialogConfig() ;
    dialogconfig.disableClose = true ;
    dialogconfig.autoFocus = true ;
    dialogconfig.width = '60%';
    // dialogconfig.data = {id: this.fieldId };
    this.dialog.open(EditProfileComponent, dialogconfig);
  }
  register() {
    this.authService.register(this.model).subscribe(
      () => { this.authService.login(this.model).subscribe(next => {this.openEditProfileForm(); });
              this.cancelRegister();
              this.alertify.success('registration successful');
            }
    , error => {this.cancelRegister();
                console.log(error.username);
                console.log(error.password);
                if (error.username) { this.alertify.error('Username : ' + error.username[0]); }
                if (error.password) { this.alertify.error('Password : ' + error.password[0]); }
               }
    );
  }

 
}
