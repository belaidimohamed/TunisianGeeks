import { ScreenShotsFormComponent } from './../_forms/ScreenShotsForm/ScreenShotsForm.component';
import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { ApiGetService } from '../_services/apiGet.service';
import { NgxGalleryOptions, NgxGalleryImage, NgxGalleryAnimation, NgxGalleryImageSize } from 'ngx-gallery';
import { MatDialog, MatDialogConfig } from '@angular/material';
import { ProjectFormComponent } from '../_forms/projectForm/projectForm.component';
import { AlertifyService } from '../_services/alertify.service';

@Component({
  selector: 'app-project',
  templateUrl: './project.component.html',
  styleUrls: ['./project.component.css']
})
export class ProjectComponent implements OnInit {
  galleryOptions: NgxGalleryOptions[];
  galleryImages: NgxGalleryImage[];
  project: any ;
  photos: any ;
  url: any;
  id: number;
  CodeHideShow = false ;
  baseUrlmedia = 'http://127.0.0.1:8000/media/';
  constructor(  private route: ActivatedRoute, private apiGetService: ApiGetService  ,
                private dialog: MatDialog , private alertify: AlertifyService ) {}



   ngOnInit() {
    this.project = this.route.snapshot.data.project ;
    this.photos = this.route.snapshot.data.photos ;
    console.log(this.photos);
    // tslint:disable-next-line: radix
    this.route.params.subscribe(params => {this.id = parseInt(params.pId); });
    this.galleryOptions = [
      {   width: '600px',
          height: '400px',
          imagePercent: 90,
          thumbnailsColumns: 4,
          imageAnimation: NgxGalleryAnimation.Slide,
          imageInfinityMove: true ,
          previewCloseOnEsc: true,
          previewKeyboardNavigation: true,
          previewDownload: true,
          imageDescription: true,
      },
      // max-width 800
      {
          breakpoint: 800,
          width: '100%',
          height: '600px',
          imagePercent: 90,
          thumbnailsPercent: 20,
          thumbnailsMargin: 20,
          thumbnailMargin: 20
      },
      // max-width 400
      {
          breakpoint: 400,
          preview: false
      }
  ];
    this.makeGallery(this.photos);

  }
  makeGallery(photo: any) {
    this.galleryImages = [] ;
    for (const i of  this.photos) {
        this.galleryImages.push(
            {
                small: this.baseUrlmedia + i.image,
                medium: this.baseUrlmedia + i.image,
                big: this.baseUrlmedia + i.image,
                description: i.legend,
            }
        );
    }
  }
  addCodeHideShow() {
    this.CodeHideShow = !this.CodeHideShow;
  }
  addPhoto() {
    const dialogconfig = new MatDialogConfig() ;
    dialogconfig.disableClose = true ;
    dialogconfig.autoFocus = true ;
    dialogconfig.width = '60%';
    dialogconfig.data = {id: this.id };
    this.dialog.open(ScreenShotsFormComponent, dialogconfig).afterClosed().subscribe(next => {
      this.apiGetService.getScreenShots(this.id).subscribe( data => {
                                                                      this.photos = data ;
                                                                      this.photos = Array.of(JSON.parse(this.photos))[0];
                                                                      console.log(this.photos);
                                                                      this.makeGallery(this.photos);
                                                          },
                                                  error => {this.alertify.error(error); });
    });
  }
}
