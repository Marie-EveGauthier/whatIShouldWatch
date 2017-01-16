<?php

/* ::base.html.twig */
class __TwigTemplate_ad69ae4284d879ac3f4328acdae0f696394841f40f879cdd4cf48e175a868c3a extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
            'title' => array($this, 'block_title'),
            'stylesheets' => array($this, 'block_stylesheets'),
            'body' => array($this, 'block_body'),
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"UTF-8\" />
        <title>";
        // line 5
        $this->displayBlock('title', $context, $blocks);
        echo "</title>
    ";
        // line 6
        $this->displayBlock('stylesheets', $context, $blocks);
        // line 7
        echo "    <link rel=\"icon\" type=\"image/x-icon\" href=\"";
        echo twig_escape_filter($this->env, $this->env->getExtension('assets')->getAssetUrl("favicon.ico"), "html", null, true);
        echo "\" />
</head>
<body>

    <ul>
        <li><a href=";
        // line 12
        echo $this->env->getExtension('routing')->getPath("tuto_test_first");
        echo "> Films </a></li>
        <li><a href=";
        // line 13
        echo $this->env->getExtension('routing')->getPath("tuto_test_second");
        echo "> Writers </a></li>
        <li><a href=\"#\"> Directors </a></li>
    </ul>
";
        // line 16
        $this->displayBlock('body', $context, $blocks);
        // line 17
        echo "</body>
</html>
";
    }

    // line 5
    public function block_title($context, array $blocks = array())
    {
        echo "Welcome!";
    }

    // line 6
    public function block_stylesheets($context, array $blocks = array())
    {
    }

    // line 16
    public function block_body($context, array $blocks = array())
    {
    }

    public function getTemplateName()
    {
        return "::base.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  72 => 16,  67 => 6,  61 => 5,  55 => 17,  53 => 16,  47 => 13,  43 => 12,  32 => 6,  22 => 1,  34 => 7,  28 => 5,);
    }
}