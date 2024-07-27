import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';


const QueryForm = () => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/query', { text: question });
      setAnswer(response.data.answer);
    } catch (error) {
      setAnswer('Error al procesar la consulta');
      console.error(error);
    }
  };

  return (
    <div className="card p-4 my-4">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            type="text"
            className="form-control"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ingresa prompt"
          />
        </div>
        <button type="submit" className="btn btn-primary mt-2">Enviar</button>
      </form>
      {answer && <p className="mt-3">Respuesta: {answer}</p>}
    </div>
  );
};

export default QueryForm;