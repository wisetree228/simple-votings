import React from 'react';

interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary';
  onClick?: () => void;
}

export const Button = ({ children, variant = 'primary', onClick }: ButtonProps) => {
  const baseStyles = "px-6 py-3 rounded-lg font-semibold transition-all duration-200 text-lg";
  const variants = {
    primary: "bg-yellow-400 hover:bg-yellow-500 text-black",
    secondary: "bg-white hover:bg-gray-100 text-black"
  };

  return (
    <button 
      className={`${baseStyles} ${variants[variant]}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
};