import { ScreenShotsFormComponent } from './_forms/ScreenShotsForm/ScreenShotsForm.component';
import { SkillFormComponent } from './_forms/skillForm/skillForm.component';
import { EditProfileComponent } from './_forms/editProfile/editProfile.component';
import { CommentResolver  } from './_resolvers/comment-resolver';
import { ProfileResolver } from './_resolvers/profile-resolver';
import { CommentsComponent } from './project/comments/comments.component';
import { PhotoResolver } from './_resolvers/screen-shots-resolver';
import { ProjectResolver } from './_resolvers/project-resolver';
import { SafePipe } from './project/SafePipe.pipe';
import { appRoutes } from './routes';
import { ErrorInterceptorProvider } from './_services/error.interceptor';

import { RouterModule } from '@angular/router';
import { BrowserModule, HammerGestureConfig, HAMMER_GESTURE_CONFIG } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { MatDialogModule } from '@angular/material/dialog';
import { NgxGalleryModule } from 'ngx-gallery';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FileUploadModule } from 'ng2-file-upload';


import { AppComponent } from './app.component';
import { ProjectComponent } from './project/project.component';
import { NavComponent } from './nav/nav.component';
import { SideNavComponent } from './side-nav/side-nav.component';
import { RegisterComponent } from './_forms/register/register.component';
import { ProjectFormComponent } from './_forms/projectForm/projectForm.component';
import { FieldFormComponent } from './_forms/fieldForm/fieldForm.component';
import { ProfileComponent } from './profile/profile.component';
import { HomeNavComponent } from './homeNav/homeNav.component';
import { AcceuilComponent } from './acceuil/acceuil.component';


export class CustomHammerConfig extends HammerGestureConfig  {
  overrides = {
      pinch: { enable: false },
      rotate: { enable: false }
  };
}
@NgModule({
  declarations: [
    AppComponent,
    ProjectComponent,
    NavComponent,
    SideNavComponent,
    RegisterComponent,
    ProfileComponent,
    FieldFormComponent,

    ProjectFormComponent,
      CommentsComponent,
      ScreenShotsFormComponent,
      SafePipe,
      HomeNavComponent,
      AcceuilComponent,
      EditProfileComponent,
      SkillFormComponent
   ],
  imports: [
    RouterModule.forRoot(appRoutes),
    FileUploadModule,
    BrowserModule,
    FormsModule,
    HttpClientModule,
    BsDropdownModule.forRoot(),
    MatDialogModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    NgxGalleryModule,
  ],
  providers: [
    ErrorInterceptorProvider,
    ProjectResolver,
    PhotoResolver,
    CommentResolver,
    ProfileResolver,
    { provide: HAMMER_GESTURE_CONFIG, useClass: CustomHammerConfig },
  ],
  bootstrap: [AppComponent],
  entryComponents: [
    RegisterComponent,
    FieldFormComponent,
    ProjectFormComponent,
    EditProfileComponent,
    ScreenShotsFormComponent,
    SkillFormComponent
  ]
})
export class AppModule { }
