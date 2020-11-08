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
  model: any = {};
  click = false ;
  comments: any ;

  onFocusComment = false ;
  onFocusCommentArea = false ;
  comment = '';
  buttonCommentMargin = 68 ;

  onclickRponse = false ;
  onFocusReponse = false ;
  onFocusReplyArea = false;
  reply = '' ;
  tab: any = {};
  buttonReplyMargin = 68 ;


  constructor(private route: ActivatedRoute, private apiPost: ApiPostService  , private router: Router,
              private apiGet: ApiGetService, private alertify: AlertifyService) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.comments = JSON.parse(this.route.snapshot.data.comments) ;
    })
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
  LikeComment(id: number) {
    console.log('like');
    const modelJ = new FormData();

    modelJ.append('uid', localStorage.getItem('id'));
    modelJ.append('id', JSON.stringify(id)) ;
    this.apiPost.addLike(modelJ).subscribe(data => { console.log(data); },
                                       error => {console.log(error); });
  }
  SendComment() {
    console.log('baw');
    this.route.params.subscribe(params => {
      this.model.project = params.pId ;
     });
    this.model.comment = this.comment ;
    // tslint:disable-next-line: radix
    this.model.user = parseInt(localStorage.getItem('id'));
    this.apiPost.addComment(this.model).subscribe(
      () => {  const dateTime = new Date();
               this.comments.push({
                 comment: this.model.comment,
                 jaims: {},
                 project_id: this.model.project,
                 username: localStorage.getItem('name'),
                 timeSent: dateTime.toISOString(),
               });
               console.log(this.comments);
               this.alertify.success('Comment sent successfully'); },
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
