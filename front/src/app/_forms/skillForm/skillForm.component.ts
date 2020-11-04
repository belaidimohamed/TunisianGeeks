import { AlertifyService } from './../../_services/alertify.service';
import { ApiPostService } from 'src/app/_services/apiPost.service';
import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialog } from '@angular/material';
import { Router, ActivatedRoute } from '@angular/router'
@Component({
  selector: 'app-skillForm',
  templateUrl: './skillForm.component.html',
  styleUrls: ['./skillForm.component.css']
})
export class SkillFormComponent implements OnInit {
  key: number ;
  constructor(private apiPost: ApiPostService , @Inject(MAT_DIALOG_DATA) public data: any , private route: ActivatedRoute,
              private dialog: MatDialog, private alertify: AlertifyService, private router: Router) { }

  ngOnInit() {
    this.key = this.data.key;
  }
  cancel() {
    this.dialog.closeAll() ;
  }

  saveSkill() {
    if (!this.data.skill) {
      this.alertify.warning('can you fill skill field please !')
    } else
    if (!this.data.percent) {
      this.alertify.warning('can you fill percentage field please !')
    } else
    if (this.data.percent < 0 || this.data.percent > 100) {
      this.alertify.warning(' percentage is between 100 and 0 -_-! ');
    } else if (isNaN(this.data.percent)) {
      this.alertify.warning(' I said percentage not a word stupid ! ');
    } else {
    // tslint:disable-next-line: radix
   
        const modelJ = new FormData();
        modelJ.append('skill',this.data.skill)
        modelJ.append('percentage',this.data.percent)
        this.apiPost.addSkill(modelJ, parseInt(localStorage.getItem('id'))).subscribe(
          next => { this.cancel();
                    this.alertify.success('Skill added succefully ');
                  },
          error => {
            this.alertify.error(error.detail);
            console.log(error.detail);
            this.cancel();
          });
      }
    } // end skill
  
saveLang() {
    if (!this.data.lang) {
      this.alertify.warning('can you fill Language field please !')
    } else
    if (!this.data.level) {
      this.alertify.warning('can you fill level field please !')
    } else {
    // tslint:disable-next-line: radix
          const modelJ = new FormData();
          modelJ.append('lang',this.data.lang)
          modelJ.append('level',this.data.level)
          this.apiPost.addLang(modelJ, parseInt(localStorage.getItem('id'))).subscribe(
            next => { this.cancel();
                      this.alertify.success('Language added succefully ');
                    },
            error => {
              this.alertify.error(error.detail);
              console.log(error.detail);
              this.cancel();
            });
      }
  } // end lang
}
