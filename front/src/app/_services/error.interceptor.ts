import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpErrorResponse, HTTP_INTERCEPTORS } from '@angular/common/http';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable()
export class ErrorInterceptor implements HttpInterceptor {
    intercept(req: import('@angular/common/http').HttpRequest<any>,
              next: import('@angular/common/http').HttpHandler):
                    import('rxjs').Observable<import('@angular/common/http').HttpEvent<any>> {
                        return next.handle(req).pipe(
                            catchError(error => {
                                if (error.status === 401) {
                                    return throwError(error.statusText); }

                                if (error instanceof HttpErrorResponse) {
                                    const ApplicationError = error.headers.get('Application-Error');
                                    if (ApplicationError) {
                                        return throwError(ApplicationError); }
                                }
                                const serverError = error.error ;
                                let modalStateError = '';
                                if (serverError.errors && typeof serverError.errors === 'object' ) {
                                    for (const key in serverError.errors ) {
                                        if (serverError.errors[key]) {
                                            modalStateError += serverError.errors[key] + '\n';
                                        }
                                    }
                                }
                                return throwError(modalStateError || serverError || 'Server Error' ) ;
                            })
                            ); }
                    }
export const ErrorInterceptorProvider = {
    provide: HTTP_INTERCEPTORS,
    useClass: ErrorInterceptor,
    multi: true
};
