import { AuthService } from './auth.service';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { GlobalConstants } from '../global-constants'
@Injectable({
  providedIn: 'root'
})
export class ApiGetService {

  values: any = {} ;
  baseUrl = GlobalConstants.apiURL ;
  headers = new HttpHeaders({
    Authorization: 'Token ' + localStorage.getItem('token')
  } );
  constructor(private http: HttpClient, private authService: AuthService) { }

  getUsers() {
    return this.http.get(this.baseUrl + 'users/' , {headers: this.headers});
  }
  getUser(id: number) {
    return this.http.get(this.baseUrl + 'users/' + id + '/' , {headers: this.headers});
  }
  getFields() {
    const id = localStorage.getItem('id') ;
    return this.http.get(this.baseUrl + 'field/' + id  + '/getFields/' , {headers: this.headers});
  }

  getProjects(id: number) {
    return this.http.get(this.baseUrl + 'project/' + id + '/getProjects/' , {headers: this.headers});
  }
  getProject(id: number) {
    return this.http.get(this.baseUrl + 'project/' + id + '/' , {headers: this.headers});
  }
  getScreenShots(id: number) {
    return this.http.get(this.baseUrl + 'photo/' + id + '/getPhotos/' , {headers: this.headers});
  }
  getComments(id: number) {
    return this.http.get(this.baseUrl + 'comment/' + id + '/getComments/' , {headers: this.headers});
  }
  getProfile(id: number) {
    return this.http.get(this.baseUrl + 'profile/' + id + '/getProfile/' , {headers: this.headers});
  }
 
}
