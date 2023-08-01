import logo from './logo.svg';
import './App.css';
import Login from './pages/login';
import ManualEntry from './pages/manualentry';
import BookSearch from './pages/booksearch';
import Banner from './components/banner';
import React, {useState} from 'react';

function App() {

  const [currentPage, setCurrentPage] = useState('BookSearch');

  const renderPage = () => {
    if (currentPage === 'Login') {
      return <Login />;
    }
    if (currentPage === 'BookSearch') {
      return <BookSearch />;
    }
    if (currentPage === 'Manualentry') {
      return <ManualEntry />;
    }
    
  };

  const handlePageChange = (page) => setCurrentPage(page);

  return (
    <div className="App">
        <Banner currentPage={currentPage} handlePageChange={handlePageChange} />
        {renderPage()}
      
    </div>
  );
}

export default App;
