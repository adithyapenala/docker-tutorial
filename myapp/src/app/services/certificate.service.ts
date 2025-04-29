import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CertificateService {
  url = 'http://localhost:5000/'
  constructor(private http: HttpClient) { }

  getCertData(appNum: string, type:"community" | "income"){
    this.http.get(this.url+type+"/"+appNum)
  }
}
