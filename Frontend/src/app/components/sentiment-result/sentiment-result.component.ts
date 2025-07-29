import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-sentiment-result',
  templateUrl: './sentiment-result.component.html',
  styleUrls: ['./sentiment-result.component.css']
})
export class SentimentResultComponent {
  @Input() sentiment: string = '';
}
