import { Component, OnInit } from '@angular/core';
import {ContactService} from '../contact.service';
import {Contact} from '../contact';

@Component({
  selector: 'app-contacts',
  templateUrl: './contacts.component.html',
  styleUrls: ['./contacts.component.css'],
  providers:[ContactService]
})
export class ContactsComponent implements OnInit {
  contacts: Contact[];
  contact: Contact;
  
     advisor_phone: string;
     sbo_phone: string;
     sbo_email: string;
     call_duration: string;
     match_sid: string;
     sbo_name: string;
     interview_date: string;
     call_sid: string;
     advisor_name: string;
     advisor_email: string;
     interview_time: string;


 
    /*first_name: string;
    last_name: string;
    phone: string;*/

  constructor(private contactService: ContactService) { }

  ngOnInit() {
    this.contactService.getcontacts()
     .subscribe(contacts =>
    this.contacts = contacts);
  }

}
