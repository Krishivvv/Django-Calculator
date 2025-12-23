# 🧮 Professional Scientific Calculator

A modern, feature-rich scientific calculator web application built with Django framework, featuring a sleek glassmorphic UI design and comprehensive mathematical operations.

## ✨ Features

### 🎯 Core Functionality
- **Dual Mode Operation**
  - Basic Calculator Mode for everyday calculations
  - Scientific Calculator Mode for advanced mathematical operations
  
- **Comprehensive Operations**
  - Basic: Addition, Subtraction, Multiplication, Division
  - Scientific: Trigonometric functions (sin, cos, tan, asin, acos, atan)
  - Advanced: Logarithms (log, ln), Square root, Power (x^y)
  - Special: Factorial, Modulo, Pi (π), Euler's number (e)
  
- **Memory Functions**
  - MC (Memory Clear)
  - MR (Memory Recall)
  - M+ (Memory Add)
  - M- (Memory Subtract)
  - MS (Memory Store)

- **Calculation History**
  - Stores last 10 calculations
  - Easy reference to previous operations
  - Clear and organized display

### 🎨 Design Features
- **Modern Glassmorphic UI** with blur effects and transparency
- **Dark/Light Theme Toggle** for comfortable viewing in any environment
- **Smooth Animations** and hover effects for enhanced user experience
- **Responsive Design** that works seamlessly on desktop, tablet, and mobile
- **Gradient Backgrounds** with professional color schemes
- **Clean, Minimalist Interface** following modern design principles

### ⌨️ User Experience
- **Keyboard Support** for faster input
  - Number keys (0-9)
  - Operators (+, -, *, /)
  - Enter for equals
  - Escape for clear
  - Backspace for delete
  
- **Parentheses Support** for complex expressions
- **Real-time Display Updates**
- **Error Handling** with clear error messages
- **Intuitive Button Layout** matching standard calculator designs

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Krishivvv/Django-Calculator
   cd django-calculator
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Navigate to project directory**
   ```bash
   cd calculator_project
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser**
   ```
   Navigate to: http://127.0.0.1:8000/
   ```

## 📁 Project Structure

```
django-calculator/
│
├── calculator_project/          # Main project directory
│   ├── calculator/              # Calculator app
│   │   ├── migrations/          # Database migrations
│   │   ├── templates/           # HTML templates
│   │   │   └── calculator/
│   │   │       └── calculator.html
│   │   ├── static/              # Static files (CSS, JS, images)
│   │   ├── __init__.py
│   │   ├── admin.py            # Admin configuration
│   │   ├── apps.py             # App configuration
│   │   ├── forms.py            # Django forms
│   │   ├── models.py           # Database models
│   │   ├── tests.py            # Unit tests
│   │   ├── urls.py             # App URLs
│   │   └── views.py            # View functions
│   │
│   ├── calculator_project/      # Project settings
│   │   ├── __init__.py
│   │   ├── asgi.py             # ASGI configuration
│   │   ├── settings.py         # Project settings
│   │   ├── urls.py             # Project URLs
│   │   └── wsgi.py             # WSGI configuration
│   │
│   └── manage.py                # Django management script
│
├── venv/                        # Virtual environment
├── README.md                    # This file
└── .gitignore                   # Git ignore file
```

## 🎮 Usage Guide

### Basic Mode
1. Click numbers to input values
2. Click operators (+, -, ×, ÷) to perform operations
3. Click "=" to calculate result
4. Click "C" to clear display

### Scientific Mode
1. Toggle to Scientific mode using the mode selector
2. Access advanced functions:
   - **Trigonometry**: sin, cos, tan (in radians)
   - **Inverse Trig**: asin, acos, atan
   - **Logarithms**: log (base 10), ln (natural log)
   - **Powers**: Use x^y button then enter exponent
   - **Constants**: π (pi), e (Euler's number)
   - **Factorial**: Enter number then click n!

### Memory Operations
1. Enter a number
2. Click MS to store in memory
3. Use M+/M- to add/subtract from memory
4. Click MR to recall memory value
5. Click MC to clear memory

### Keyboard Shortcuts
- `0-9`: Number input
- `+, -, *, /`: Basic operators
- `.`: Decimal point
- `Enter`: Calculate result
- `Escape`: Clear display
- `Backspace`: Delete last character

### Theme Toggle
- Click the 🌓 button to switch between light and dark themes
- Your preference is maintained during the session

## 🔧 Customization

### Changing Colors
Edit the CSS in the `<style>` section of `calculator.html`:
```css
/* Light mode gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Dark mode gradient */
background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
```

### Adding New Functions
1. Add button in HTML
2. Create function in JavaScript
3. Handle calculation logic

### Modifying Button Layout
Adjust the grid in CSS:
```css
.scientific-mode {
    grid-template-columns: repeat(5, 1fr); /* Change number of columns */
}
```

## 🧪 Testing

Run the test suite:
```bash
python manage.py test calculator
```

## 📦 Deployment

### Heroku Deployment
1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn calculator_project.wsgi
   ```
3. Create `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```
4. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

5. Configure firewall and SSL

## �
