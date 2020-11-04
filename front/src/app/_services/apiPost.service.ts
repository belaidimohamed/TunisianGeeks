import { AuthService } from './auth.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core'; 
import { GlobalConstants } from '../global-constants'

@Injectable({
  providedIn: 'root'
})
export class ApiPostService {
  headers = new HttpHeaders({
    'Content-type': 'application/json',
    Authorization: 'Token ' + localStorage.getItem('token')
  } );
  headers1 = new HttpHeaders({
    Authorization: 'Token ' + localStorage.getItem('token')
  } );

  constructor(private http: HttpClient, private authService: AuthService) { }
  baseUrl = GlobalConstants.apiURL ;

  AddField(model: any) {
    return this.http.post(this.baseUrl + 'field/', model, { headers: this.headers});
  }
  AddProject(model: any) {
    return this.http.post(this.baseUrl + 'project/', model, { headers: this.headers1});
  }
  AddScreenShot(model: any) {
    return this.http.post(this.baseUrl + 'photo/', model, { headers: this.headers1});
  }

  addComment(model: any) {
    return this.http.post(this.baseUrl + 'comment/', model, { headers: this.headers});
  }
  addLike(model: any) {
    return this.http.post(this.baseUrl + 'likeComment/' , model , { headers: this.headers1 });
  }
  AddProfile(model: any , id: number) {
    return this.http.post(this.baseUrl + 'profile/' + id + '/editProfile/', model, { headers: this.headers1 });
  }
  addSkill(model: any , id: number) {
    return this.http.post(this.baseUrl + 'profile/' + id + '/addSkill/' , model , {headers: this.headers1});
  }
  addLang(model:any , id:number ) {
    return this.http.post(this.baseUrl + 'profile/' + id + '/addLang/' , model , {headers: this.headers1});
  }
};
