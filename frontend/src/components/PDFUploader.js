import React, { useState } from 'react';
import axios from 'axios';

const PDFUploader = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      setMessage('Por favor selecciona un archivo PDF');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/upload-pdf/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setMessage(response.data.info);
    } catch (error) {
      setMessage('Error al cargar el archivo');
      console.error(error);
    }
  };

  return (
    <div className="card p-4 my-4">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <input type="file" className="form-control" onChange={handleFileChange} accept=".pdf" />
        </div>
        <button type="submit" className="btn btn-primary mt-2">Subir PDF</button>
      </form>
      {message && <p className="mt-3">{message}</p>}
    </div>
  );
};

export default PDFUploader;