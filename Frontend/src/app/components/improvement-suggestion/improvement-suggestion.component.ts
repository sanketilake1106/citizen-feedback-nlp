import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-improvement-suggestion',
  templateUrl: './improvement-suggestion.component.html',
  styleUrl: './improvement-suggestion.component.css'
})
export class ImprovementSuggestionComponent {
   @Input() improvements: string[] | undefined;
}
