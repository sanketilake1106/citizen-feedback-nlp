import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { FeedbackFormComponent } from './components/feedback-form/feedback-form.component';
import { SentimentResultComponent } from './components/sentiment-result/sentiment-result.component';
import { TopicListComponent } from './components/topic-list/topic-list.component';
import { ImprovementSuggestionComponent } from './components/improvement-suggestion/improvement-suggestion.component';

@NgModule({
  declarations: [
    AppComponent,
    FeedbackFormComponent,
    SentimentResultComponent,
    TopicListComponent,
    ImprovementSuggestionComponent
  ],
  imports: [BrowserModule, FormsModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
