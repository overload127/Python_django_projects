import { TestBed } from '@angular/core/testing';

import { BbService } from './bb.service';

describe('BbService', () => {
  let service: BbService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BbService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
