import { ProfileResolver } from './_resolvers/profile-resolver';
import { AcceuilComponent } from './acceuil/acceuil.component';
import { HomeNavComponent } from './homeNav/homeNav.component';
import { CommentResolver } from './_resolvers/comment-resolver';
import { PhotoResolver } from './_resolvers/screen-shots-resolver';
import { ProjectResolver } from './_resolvers/project-resolver';
import { ProjectComponent } from './project/project.component';
import { ProfileComponent } from './profile/profile.component';
import { NavComponent } from './nav/nav.component';
import { SideNavComponent } from './side-nav/side-nav.component';

import { Routes } from '@angular/router';

export const appRoutes: Routes = [
    { path: 'home', component: HomeNavComponent},
    { path: 'acceuil', component: AcceuilComponent},

    { path: 'myspace', component: NavComponent},
    { path: 'field/:id', component: SideNavComponent ,
      runGuardsAndResolvers: 'always',
      children: [{
        path: 'project/:pId', component: ProjectComponent ,
        resolve: { project: ProjectResolver , photos: PhotoResolver , comments: CommentResolver}
      } ] ,
    },

    { path: 'profile/:uid', component: ProfileComponent,
      runGuardsAndResolvers: 'always',
      resolve: { profile: ProfileResolver }},
    { path: '**', redirectTo: 'home' , pathMatch: 'full'}


];
