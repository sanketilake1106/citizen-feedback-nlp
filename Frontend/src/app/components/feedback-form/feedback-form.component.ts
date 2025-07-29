import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-feedback-form',
  templateUrl: './feedback-form.component.html',
  styleUrl: './feedback-form.component.css'
})
export class FeedbackFormComponent {
  feedbackText = '';
  result: any = null;

  constructor(private api: ApiService) {}

  submitFeedback() {
    if (!this.feedbackText) return;
    this.api.analyzeFeedback(this.feedbackText).subscribe((res) => {
      this.result = res;
    });
  }
}
