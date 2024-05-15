// pages/_app.jsx
import React from 'react';
import App from 'next/app';
import '../styles/globals.css';  // Import global CSS file

class MyApp extends App {
  render() {
    const { Component, pageProps } = this.props;
    return <Component {...pageProps} />;
  }
}

export default MyApp;
