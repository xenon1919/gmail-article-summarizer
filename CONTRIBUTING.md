# 🤝 Contributing to Gmail Article Summarizer

Thank you for your interest in contributing to this project! This is a community-driven project, and we welcome contributions from everyone.

## 🚀 How to Contribute

### **1. Fork the Repository**
- Click the "Fork" button on the GitHub repository page
- Clone your forked repository to your local machine

### **2. Create a Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

### **3. Make Your Changes**
- Write clean, well-documented code
- Follow the existing code style
- Add comments for complex logic
- Test your changes thoroughly

### **4. Commit Your Changes**
```bash
git add .
git commit -m "feat: add new RSS feed source"
```

### **5. Push to Your Fork**
```bash
git push origin feature/your-feature-name
```

### **6. Create a Pull Request**
- Go to your forked repository on GitHub
- Click "New Pull Request"
- Select your feature branch
- Write a clear description of your changes

## 📋 Contribution Guidelines

### **Code Style**
- Use **Python 3.8+** syntax
- Follow **PEP 8** style guidelines
- Use meaningful variable and function names
- Add type hints where appropriate

### **Documentation**
- Update README.md if adding new features
- Add docstrings to new functions
- Include examples for new functionality

### **Testing**
- Test your changes with different RSS feeds
- Verify email sending works correctly
- Check that error handling is robust

## 🎯 Areas for Contribution

### **High Priority**
- 🆕 **New RSS Feed Sources**: Add more tech news sources
- 🔧 **Bug Fixes**: Fix any issues you encounter
- 📧 **Email Templates**: Improve email formatting
- 🤖 **AI Models**: Add support for more free AI services

### **Medium Priority**
- 🎨 **UI Improvements**: Better email styling
- 📊 **Analytics**: Add usage statistics
- 🔍 **Content Filtering**: Improve relevance algorithms
- 📱 **Mobile Optimization**: Better mobile email display

### **Low Priority**
- 🌐 **Web Interface**: Create a web dashboard
- 📱 **Mobile App**: Native mobile application
- 🔔 **Notifications**: Push notifications
- 📈 **Advanced Analytics**: Detailed usage reports

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment Details**
   - Operating System
   - Python version
   - Package versions

2. **Steps to Reproduce**
   - Clear step-by-step instructions
   - Sample RSS feed URLs (if relevant)

3. **Expected vs Actual Behavior**
   - What you expected to happen
   - What actually happened

4. **Error Messages**
   - Full error traceback
   - Any log files

## 💡 Feature Requests

When requesting features, please:

1. **Describe the Problem**
   - What issue are you trying to solve?
   - Why is this feature needed?

2. **Propose a Solution**
   - How should this feature work?
   - Any specific requirements?

3. **Consider Alternatives**
   - Are there existing solutions?
   - Could this be implemented differently?

## 🔧 Development Setup

### **Local Development**
```bash
# Clone the repository
git clone https://github.com/your-username/gmail-article-summarizer.git
cd gmail-article-summarizer

# Install dependencies
pip install -r requirements_gmail.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your credentials

# Run tests
python test_gmail.py
```

### **Testing Your Changes**
```bash
# Test the main script
python article_summarizer_gmail.py

# Test manual run
python manual_run.py

# Test demo
python demo_gmail.py
```

## 📝 Commit Message Guidelines

Use conventional commit messages:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

Example:
```
feat: add support for Medium RSS feeds
fix: resolve Gmail authentication timeout
docs: update README with new features
```

## 🏷️ Pull Request Template

When creating a PR, please include:

### **Description**
Brief description of changes

### **Type of Change**
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

### **Testing**
- [ ] Tested manually
- [ ] Added unit tests
- [ ] All tests pass

### **Screenshots** (if applicable)
Add screenshots for UI changes

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

## 📞 Questions?

If you have questions about contributing:
- Open an issue for general questions
- Join our discussions for feature planning
- Check existing issues for similar questions

---

**Thank you for contributing to making this project better! 🚀**
