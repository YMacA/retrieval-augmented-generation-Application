import logo from './logo.svg';
import './App.css';
import React from 'react';
import PDFUploader from './components/PDFUploader';
import QueryForm from './components/QueryForm';

function App() {
  return (
    <div className="App container">
      <h1 className="my-4">Sistema RAG</h1>
      <PDFUploader />
      <QueryForm />
    </div>
  );
}

export default App;
