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
   Advisor: string;
    AdvisorPhone: string;
    AdvisorEmail: string;
    SBO: string;
    SBOemail: string;
    SBOPhone: string;
    interview_date: string;
    Time: string;
    AdvisorInitiates : string;

 
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
