import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SignInComponent} from "./auth/sign-in/sign-in.component";
import {SignUpComponent} from "./auth/sign-up/sign-up.component";
import {ForgotPasswordComponent} from "./auth/forgot-password/forgot-password.component";
import {LayoutComponent} from "./layout/layout.component";

const routes: Routes = [
  {
    path:'sign-in',
    component:SignInComponent
  },
  {
    path:'sign-up',
    component:SignUpComponent
  },
  {
    path:'forgot-password',
    component:ForgotPasswordComponent
  },
  {
    path:'',
    component:LayoutComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
