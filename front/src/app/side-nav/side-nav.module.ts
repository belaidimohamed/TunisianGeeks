import { NavComponent } from './../nav/nav.component';
import { appRoutes } from './../routes';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SideNavComponent } from './side-nav.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    RouterModule.forRoot(appRoutes),
    CommonModule

  ],
  declarations: [SideNavComponent,NavComponent]
})
export class SideNavModule { }
