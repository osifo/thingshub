import React, { Component } from 'react';

class ErrorBoundary extends Component {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true }
  }

  componentDidCatch(error, info) {
    console.log('An error has occurred in this component ==== ', error, info)
  }

  render () {
    console.log('this.state.hasError ======= ', this.state.hasError)
    console.log('notification ======= ', this.props.notification)
    return this.state.hasError ? (
      <div><h2>{this.props.notification}</h2></div>
    ) : this.props.children
  }
}

export default ErrorBoundary;