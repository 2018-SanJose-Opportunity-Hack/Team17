import { Injectable } from '@angular/core';
import {Http, Headers} from '@angular/http';
import {Contact} from './contact';
import 'rxjs/add/operator/map';
import {Observable}     from 'rxjs/Observable';
import 'rxjs/add/operator/do';
@Injectable()
export class ContactService {

  constructor(private http:Http) { }


  getcontacts(){
    console.log("going");
    return this.http.get('https://b11e976e.ngrok.io/get_logs')
    .map(res => res.json())
    .do(value => console.log(value));
  }
}
