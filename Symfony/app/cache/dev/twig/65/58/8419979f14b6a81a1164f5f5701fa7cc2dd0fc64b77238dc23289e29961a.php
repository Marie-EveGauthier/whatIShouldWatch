<?php

/* TutoTestBundle:Default:index.html.twig */
class __TwigTemplate_65588419979f14b6a81a1164f5f5701fa7cc2dd0fc64b77238dc23289e29961a extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

<<<<<<< HEAD
        $this->parent = $this->env->loadTemplate("::base.html.twig");

        $this->blocks = array(
            'body' => array($this, 'block_body'),
        );
    }

    protected function doGetParent(array $context)
    {
        return "::base.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $this->parent->display($context, array_merge($this->blocks, $blocks));
    }

    // line 2
    public function block_body($context, array $blocks = array())
    {
=======
        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "the name of the film is ";
        echo twig_escape_filter($this->env, (isset($context["film"]) ? $context["film"] : $this->getContext($context, "film")), "html", null, true);
        echo "! <br>
the realisator of the film is ";
        // line 2
        echo twig_escape_filter($this->env, (isset($context["realisator"]) ? $context["realisator"] : $this->getContext($context, "realisator")), "html", null, true);
        echo "!
";
>>>>>>> upstream/dev
    }

    public function getTemplateName()
    {
        return "TutoTestBundle:Default:index.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
<<<<<<< HEAD
        return array (  28 => 2,);
=======
        return array (  24 => 2,  19 => 1,);
>>>>>>> upstream/dev
    }
}
