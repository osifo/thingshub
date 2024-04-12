import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Dashboard from './pages/Dashboard';
import AccountSettings from './pages/AccountSettings'
import AddNewDevice from './pages/AddDevice'

const App = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: { retry: 2 }
    }
  });

  return (
    <BrowserRouter>
      <QueryClientProvider client={queryClient}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/accounts" element={<AccountSettings />} />
          <Route path ="/new-device" element={<AddNewDevice />} />
          {/* <Route path="/devices" element={<Devices />} />
          <Route path="/devices/:id" element={<DeviceDetails />} /> */}
        </Routes>
      </QueryClientProvider>
    </BrowserRouter>
  )
};

const container = document.getElementById("root");
const root = createRoot(container);

root.render(<App />);
