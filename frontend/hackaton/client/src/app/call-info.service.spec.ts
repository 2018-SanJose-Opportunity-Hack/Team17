/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { CallInfoService } from './call-info.service';

describe('CallInfoService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CallInfoService]
    });
  });

  it('should ...', inject([CallInfoService], (service: CallInfoService) => {
    expect(service).toBeTruthy();
  }));
});
