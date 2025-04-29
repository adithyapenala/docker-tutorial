import { Routes } from '@angular/router';
import { CertificatesComponent } from './forms/certificates/certificates.component';
export const routes: Routes = [
    {path: '', component: CertificatesComponent},
    {path: '/cert', component: CertificatesComponent},
];
