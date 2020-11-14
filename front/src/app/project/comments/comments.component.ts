import { GlobalConstants } from './../../global-constants';
import { AuthService } from './../../_services/auth.service';
import { AlertifyService } from 'src/app/_services/alertify.service';
import { ActivatedRoute , Router } from '@angular/router';
import { ApiGetService } from './../../_services/apiGet.service';
import { ApiPostService } from 'src/app/_services/apiPost.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.css']
})
export class CommentsComponent implements OnInit {
  pid: number ;
  like: any = {} ;
  model: any = {};
  click = false ;
  comments: any ;
  project: any ;
  onFocusComment = false ;
  onFocusCommentArea = false ;
  comment = '';
  buttonCommentMargin = 68 ;
  baseUrlmedia = GlobalConstants.apiURL + 'media/';

  onclickRponse = false ;
  onFocusReponse = false ;
  onFocusReplyArea = false;
  reply = '' ;
  tab: any = {};
  buttonReplyMargin = 68 ;


  constructor(private route: ActivatedRoute, private apiPost: ApiPostService  , private router: Router,
              private apiGet: ApiGetService, private alertify: AlertifyService) { }

  ngOnInit() {
    // tslint:disable-next-line: radix
    this.route.params.subscribe(data => { this.pid = data.pId; });
    this.apiGet.getComments(this.pid).subscribe((data: string) => {
      this.comments = JSON.parse(data) ;
    });
  }

  // --------------------------------------------- comment shit ---------------------------------------------

  FocusComment() {
    if (!this.click) { // Because focusout interfere with click, we use mousedown .
    // and because focusout occure after the mousedown we need to block it whenever we click the button(mousedown)
    this.onFocusCommentArea = !this.onFocusCommentArea;
    if (this.comment == '') { // nothing happened
      this.onFocusComment = ! this.onFocusComment ;
      this.buttonCommentMargin = 68;
    } else if (this.comment != '' && this.onFocusCommentArea) { // area full width , text dirty
      this.buttonCommentMargin = 68;
    } else { // text dirty
      this.buttonCommentMargin = 18;
    }
   } else {
    this.click = !this.click ;
  }
  }
  cancelComment() {
    this.comment = '' ;
    this.onFocusComment = false ;
    this.onFocusCommentArea = false ;
    this.click = true ;
  }
  LikeComment(cid: number) {
    this.like.commentId = cid ;
    // tslint:disable-next-line: radix
    this.like.userId = parseInt(localStorage.getItem('id'));
    this.apiPost.addLike(this.like, this.pid).subscribe(
      () => {
              this.apiGet.getComments(this.pid).subscribe((data: string) => {
                this.comments = JSON.parse(data) ;
              });
      },
      error => {
        console.log(error);
        this.alertify.error(error); },
     );
  }
  SendComment() {

    this.model.comment = this.comment ;
    // tslint:disable-next-line: radix
    this.model.user = parseInt(localStorage.getItem('id'));
    this.model.jaims = [] ;
    this.model.reponses = {} ;
    this.model.time = new Date();

    this.apiPost.addComment(this.model, this.pid).subscribe(
      () => { this.alertify.success('Comment sent successfully');
              this.apiGet.getComments(this.pid).subscribe((data: string) => {
                this.comments = JSON.parse(data) ;
              });
      },
      error => {
        console.log(error);
        this.alertify.error(error); },
    );
    this.cancelComment();
  }
  // --------------------------------------------- Reponse shit ---------------------------------------------

  clickReply() {
    this.onclickRponse = ! this.onclickRponse ;
  }
  FocusReponse() {
    this.onFocusReplyArea = !this.onFocusReplyArea;

    if (this.reply == '') {
      this.onFocusReponse = ! this.onFocusReponse ;
    } else if (this.reply != '' && this.onFocusReplyArea) {
      this.buttonReplyMargin = 68;
    } else {
      this.buttonReplyMargin = 18;
    }
  }
  cancelReply() {
    this.reply = '' ;
    this.onFocusReponse = false ;
    this.onFocusReplyArea = false ;
  }

}
