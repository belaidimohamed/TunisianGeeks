import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { GlobalConstants } from '../global-constants'

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  baseUrl = GlobalConstants.apiURL ;
  username: string;
  s = 0;
  constructor(private http: HttpClient) { }
  login(model: any) {
    this.username = model.username  ;
    return this.http.post(this.baseUrl + 'api/token/', model).pipe(
      map((response: any) => { const token = response ;
                               if (token) {
                         localStorage.setItem('name', token.name);
                         localStorage.setItem('token', token.token);
                         localStorage.setItem('id', token.user_id);
                         console.log(token);
                       }})
    );
  }

  register(model: any) {
    return this.http.post(this.baseUrl + 'users/', model);
  }
  loggedIn() {
    const token = localStorage.getItem('token');
    if (!token) {
      return false;
    } else {
      return true;
    }
  }


}
