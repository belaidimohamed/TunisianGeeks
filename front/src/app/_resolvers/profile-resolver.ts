import { ApiGetService } from '../_services/apiGet.service';
import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot } from '@angular/router';
import { map } from 'rxjs/operators';

@Injectable()
export class ProfileResolver implements Resolve<any> {
  constructor(private api: ApiGetService) { }

  resolve(route: ActivatedRouteSnapshot) {
    return this.api.getProfile(parseInt(route.paramMap.get('uid'))).pipe(
        map(results => {
          return results;
        })); }
}
