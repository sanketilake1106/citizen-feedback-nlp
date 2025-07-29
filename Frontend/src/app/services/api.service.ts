import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ApiService {
  private baseUrl = 'http://localhost:5000/api';

  constructor(private http: HttpClient) {}

  analyzeFeedback(text: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/analyze-feedback`, { text });
  }
}
