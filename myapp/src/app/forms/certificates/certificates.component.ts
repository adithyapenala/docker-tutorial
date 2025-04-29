import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { CertificateService } from '../../services/certificate.service';

@Component({
  selector: 'app-certificates',
  imports: [CommonModule],
  templateUrl: './certificates.component.html',
  styleUrl: './certificates.component.css'
})
export class CertificatesComponent {
  toggleCerts: boolean = false;
  response: string = "";

  constructor(private service: CertificateService) {

  }
  
  toggleCert() {
    !this.toggleCert;
  }

  
}
