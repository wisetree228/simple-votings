import React from 'react';
import { Header } from './components/Header';
import { Footer } from './components/Footer';
import { MainContent } from './components/MainContent';

function App() {
  return (
    <div className="min-h-screen bg-black flex flex-col">
      <Header />
      <main className="flex-grow flex items-center justify-center">
        <MainContent />
      </main>
      <Footer />
    </div>
  );
}

export default App;