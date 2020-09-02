import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css', '../app.component.css']
})
export class LogInComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  login(username: string, password: string) {
    // TODO: Replace with proper implementation
    console.log(username)
    console.log(password)
  }

}
