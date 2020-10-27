import { Component, OnInit, Inject } from '@angular/core';
import { ApiPostService } from 'src/app/_services/apiPost.service';
import { MatDialog } from '@angular/material';
import { AlertifyService } from 'src/app/_services/alertify.service';
import {MAT_DIALOG_DATA} from '@angular/material/dialog';
@Component({
  selector: 'app-editProfile',
  templateUrl: './editProfile.component.html',
  styleUrls: ['./editProfile.component.css']
})
export class EditProfileComponent implements OnInit {
  profilePic: File;
  fullname: string ;
  sex: string ;
  bio: string ;
  adress: string ;
  phone: string ;
  email: string;
  about: string ;
  skill: any;
  constructor(private apiPostService: ApiPostService , private dialog: MatDialog , private alertify: AlertifyService
    ,         @Inject(MAT_DIALOG_DATA) public data: any) { }

  ngOnInit() {
  }
  cancelForm(k: number) {
    this.dialog.closeAll() ;
    if (k==0){
    alert('Skipping making a profile may cause some problem !! \n It\'s recommanded to create one .\
     \n You can do that form EditProfile button after clicking your name in the navbar');}
  }
  onFileChange(event: any) {
    console.log(event);
    this.profilePic =  event.target.files[0];
    console.log(this.profilePic);

  }
  onBioChange(event: any) {
    this.bio = event.target.value;
  }
  onAdressChange(event: any) {
    this.adress = event.target.value;
  }
  onPhoneChange(event: any) {
    this.phone = event.target.value;
  }
  onEmailChange(event: any) {
    this.email = event.target.value;
  }
  onSexChange(event: any) {
    this.sex = event.target.value;
  }
  onfullChange(event: any) {
    this.fullname = event.target.value ;
  }
  addProject() {
    const model = new FormData();
    model.append('bio', this.bio)  ;
    model.append('adress', this.adress)  ;
    model.append('profilePicture', this.profilePic , this.profilePic.name);

    model.append('email', this.email)  ;
    model.append('phone', this.phone)  ;
    model.append('sex', this.sex)  ;
    model.append('fullname', this.fullname)  ;

    console.log(model);

    // tslint:disable-next-line: radix
    this.apiPostService.AddProfile(model, parseInt(localStorage.getItem('id')) ).subscribe(
      res => {  console.log(res);
                this.cancelForm(1);
                this.alertify.success('Profile added successfully'); },
      error => {
        console.log(error);
        this.cancelForm(1);
        this.alertify.error(error); }
    );
}
}
