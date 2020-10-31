import { ApiGetService } from '../_services/apiGet.service';
import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot } from '@angular/router';
import { map, take } from 'rxjs/operators';

@Injectable()
export class ProjectResolver implements Resolve<any> {
  constructor(private api: ApiGetService) { }

  resolve(route: ActivatedRouteSnapshot) {
    // tslint:disable-next-line: radix
    return this.api.getProject(parseInt(route.paramMap.get('pId'))).pipe(
        map(results => {
          return results;
        })); }
}
