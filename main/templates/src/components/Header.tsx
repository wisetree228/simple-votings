import React from 'react';
import { Vote } from 'lucide-react';

export const Header = () => {
  return (
    <header className="bg-gray-800 py-4 px-6">
      <div className="container mx-auto flex items-center">
        <Vote className="text-yellow-400 w-8 h-8 mr-2" />
        <span className="text-white text-2xl font-bold">SimpleVotes</span>
      </div>
    </header>
  );
};