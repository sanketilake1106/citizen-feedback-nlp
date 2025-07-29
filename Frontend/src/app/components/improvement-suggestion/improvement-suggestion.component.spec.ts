import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImprovementSuggestionComponent } from './improvement-suggestion.component';

describe('ImprovementSuggestionComponent', () => {
  let component: ImprovementSuggestionComponent;
  let fixture: ComponentFixture<ImprovementSuggestionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ImprovementSuggestionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ImprovementSuggestionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
