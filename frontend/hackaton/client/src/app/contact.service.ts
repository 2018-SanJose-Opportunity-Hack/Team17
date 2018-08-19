import { Injectable } from '@angular/core';
import {Http, Headers} from '@angular/http';
import {Contact} from './contact';
import 'rxjs/add/operator/map';

@Injectable()
export class ContactService {

  constructor(private http:Http) { }


  getcontacts(){
    return this.http.get('http://localhost:3000/api/contacts')
    .map(res => res.json());
  }
}
