import { ApiGetService } from '../_services/apiGet.service';
import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot } from '@angular/router';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable()
export class CommentResolver implements Resolve<any> {
  constructor(private api: ApiGetService) { }

  resolve(route: ActivatedRouteSnapshot) {
    return this.api.getComments(parseInt(route.paramMap.get('pId'))).pipe(
        map(results => {
          return results;
        })); }
}
